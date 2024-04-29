<template>
<div>
<el-container>
     <el-main>
	<el-button @click="select" text :type="btnId === btn.id ? 'primary' : 'default'" class="btn" v-for="btn in btns" :btn-id="btn.id" :key="btn.id">{{ btn.text }}</el-button>
     </el-main>
</el-container>
</div>
</template>

<script setup>
import { ref } from 'vue'

let btns = [
{id: 1, text:"全站"},
{id: 2, text:"国创相关"},
{id: 3, text:"动画"},
{id: 4, text:"音乐"},
{id: 5, text:"舞蹈"},
{id: 6, text:"游戏"},
{id: 7, text:"知识"},
{id: 8, text:"科技"},
{id: 9, text:"运动"},
{id: 10, text:"汽车"},
{id: 11, text:"生活"},
{id: 12, text:"美食"},
{id: 13, text:"动物圈"},
{id: 14, text:"鬼畜"},
{id: 15, text:"时尚"},
{id: 16, text:"娱乐"},
{id: 17, text:"影视"},
{id: 18, text:"原创"},
{id: 19, text:"新人"}
]

const emit = defineEmits(['selected'])
const btnId = ref(-1)

function select(e) {
	const id = parseInt(e.currentTarget.attributes.getNamedItem('btn-id').value)
	emit('selected', id)
	btnId.value = id
}

</script>

<style scoped>
.el-container {
  position: fixed;
  top: 0;
  width: 100%;
  left:0;
  z-index: 999;
  background: skyblue;
}

.el-main {
  display: flex;
  justify-content: space-around;
  border-bottom: solid 10px;
}

</style>