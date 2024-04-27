<template>
<el-container>
	<el-header>
		<Bar @selected="updateSelectedId"/>
	</el-header>
	<el-main>
		<Content style="margin: 1rem;" v-bind:selectedId="selectedId" v-if="selectedId != -1"/>
		<el-empty v-else description="请选择一个分类"/>
	</el-main>
</el-container>
</template>

<script setup>
import { ref } from 'vue'
import Bar from './components/Bar.vue'
import Content from './components/Content.vue'

let selectedId = ref(-1)
function updateSelectedId(id) {
	 selectedId.value = id
}
</script>

<style scoped>

</style>

<style>
body {
     align-items: start;
}
</style>