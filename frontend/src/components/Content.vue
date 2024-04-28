<template>
<div>
	<el-container v-if="data['title'].length > 0">
		<el-main style="border: solid">
		       <el-row>
		               <el-col>
				       <el-text class="mx-1" type="info">总播放量</el-text>
				       <el-button @click="selectCategory" :type="selectedCategory === 'view' ? 'primary' : 'default'" text>{{data['view'].reduce((a, c) => a + c, 0)}}</el-button>
			       </el-col>
			       <el-col>
				       <el-text class="mx-1" type="info">总弹幕数</el-text>
				       <el-button @click="selectCategory" :type="selectedCategory === 'danmaku' ? 'primary' : 'default'" text>{{data['danmaku'].reduce((a, c) => a + c, 0)}}</el-button>
			       </el-col>
			       <el-col>
				       <el-text class="mx-1" type="info">总收藏数</el-text>
				       <el-button @click="selectCategory" :type="selectedCategory === 'favorite' ? 'primary' : 'default'" text>{{data['favorite'].reduce((a, c) => a + c, 0)}}</el-button>
			       </el-col>
			       <el-col>
				       <el-text class="mx-1" type="info">总投币数</el-text>
				       <el-button @click="selectCategory" :type="selectedCategory === 'coin' ? 'primary' : 'default'" text>{{data['coin'].reduce((a, c) => a + c, 0)}}</el-button>
			       </el-col>
			       <el-col>	
				       <el-text class="mx-1" type="info">总分享数</el-text>
				       <el-button @click="selectCategory" :type="selectedCategory === 'share' ? 'primary' : 'default'" text>{{data['share'].reduce((a, c) => a + c, 0)}}</el-button>
			       </el-col>
		       </el-row>
		       <el-row v-for="i in data[selectedCategory].length">
       		      	       <el-col :span="3" >
			           <el-text class="mx-1" type="primary">{{ data['author'][i-1]['name'] + '：' }}</el-text>
			       </el-col>
	       	       	       <el-col :span="8">
			           <el-text class="mx-1" type="primary">{{ data['title'][i-1] }}</el-text>
			       </el-col>
			       <el-col>
			           <el-progress :show-text=false :stroke-width="26" :percentage="data[selectedCategory][i-1]/data[selectedCategory].reduce((a, c) => a + c, 0)*100" />
			       </el-col>
			       <el-col class="detailNum" :span="1" style="margin-left: 1rem;"><el-text class="mx-1">{{ data[selectedCategory][i-1] }}</el-text></el-col>
		       </el-row>
		</el-main>
		<el-aside>
			<el-row v-for="pie in pies">
				<el-image :fit="fit" :src="pie"></el-image>
			</el-row>
		</el-aside>
	</el-container>
	<el-empty v-else description="正在加载..."/>
</div>
</template>

<script setup>

import { computed, ref, onMounted, watch } from 'vue'

const props = defineProps(['selectedId'])
const selectedId = computed(() => props.selectedId)
const data = ref({
      'title': [],
      'view': [],
      'danmaku': [],
      'favorite': [],
      'coin': [],
      'share': [],
      'author': []
})
const table = {
 	    1:"qz",
            2:"gcxg",
       	    3:"dh",
       	    4:"yy",
       	    5:"wd",
       	    6:"yx",
       	    7:"zs",
       	    8:"kj",
       	    9:"yd",
       	    10:"qc",
       	    11:"sh",
       	    12:"ms",
       	    13:"dwq",
       	    14:"gc",
       	    15:"ss",
       	    16:"yl",
       	    17:"ys",
       	    18:"yc",
       	    19:"xr",
 	    "qz":1,
            "gcxg":2,
       	    "dh":3,
       	    "yy":4,
       	    "wd":5,
       	    "yx":6,
       	    "zs":7,
       	    "kj":8,
       	    "yd":9,
       	    "qc":10,
       	    "sh":11,
       	    "ms":12,
       	    "dwq":13,
       	    "gc":14,
       	    "ss":15,
       	    "yl":16,
       	    "ys":17,
       	    "yc":18,
       	    "xr":19
}

const selectedCategory = ref("view")
const pies = computed(() => {
    let res = []
    for (let fm = 1; fm <= 100; fm += 10) {
        const to = fm + 9
        const id = props.selectedId
        const category = selectedCategory.value
        res.push("/api/" + table[id] + "?type=pie&sub=" + category + "&from=" + fm + "&to=" + to)
    }
    return res
})

function selectCategory(e) {
	 const name = e.currentTarget.previousElementSibling.textContent;
	 const table = {
	       '总播放量': 'view',
	       '总弹幕数': 'danmaku',
	       '总收藏数': 'favorite',
	       '总投币数': 'coin',
	       '总分享数': 'share',	       
	 }
	 selectedCategory.value = table[name]
}

async function fetchData() {
      const selectedId = props.selectedId
      const res = await	fetch("/api/" + table[selectedId]);
      if(selectedId == props.selectedId)
      		    data.value = await res.json()
}

onMounted(() => {
	     fetchData()
})

watch(selectedId, (n, o) => {
             data.value = {
      	       'title': [],
      	       'view': [],
      	       'danmaku': [],
      	       'favorite': [],
      	       'coin': [],
      	       'share': [],
      	       'author': []
	     }
	     fetchData()
})

</SCRIPT>

<style scoped>
.el-row {
	justify-content: center;
	margin: 1rem;
	
}
.el-col {
	flex: 1;
	flex-direction: column;
}
.el-text {
	display: block;
}
.el-button {
	font-size: 1.2rem;
}

.el-aside {
 	border: solid;
	margin-left: 1rem;
	justify-content: space-around;
	display: flex;
	flex-direction: column;
}

.detailNum {
	white-space: nowrap;
}

</style>