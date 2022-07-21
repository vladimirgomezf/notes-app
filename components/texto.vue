<template>
    <div>
        <div class="inline-flex" v-for="item in complete" :key="item">
        <!-- {{Object.values(item)[0]}} -->
            <!-- <a href="" class="bg-violet-400 rounded-2xl p-1">{{Object.entries(item)[0][0]}}</a> -->
            <span v-if="Object.entries(item)[0][0] === 'tag'" class="bg-violet-400 rounded-full px-3 bg-opacity-50">{{Object.values(item)[0]}}</span>
            <span v-if="Object.entries(item)[0][0] === 'people'" class="bg-green-300 rounded-full px-3 bg-opacity-50">{{Object.values(item)[0]}}</span>
            <span v-if="Object.entries(item)[0][0] === 'mail'" class="bg-orange-300 rounded-full px-3 bg-opacity-50">{{Object.values(item)[0]}}</span>
            <span v-if="Object.entries(item)[0][0] === 'link'" class="bg-sky-300 rounded-full px-3 bg-opacity-50">{{Object.values(item)[0]}}</span>
            <span v-if="Object.entries(item)[0][0] === 'text'">{{Object.values(item)[0]}}</span>
            &nbsp;
        </div>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                complete: []
            };
        },
        props: {
            text: ""
        },
        mounted(){
            this.separe()
        },
        methods: {
            separe(){
                const words = this.text.split(" ");
                words.forEach(i => {
                    if (i[0] === "#") {
                        this.complete.push({"tag": i})
                    }else if (i[0] === "@"){
                        this.complete.push({"people": i})
                    }else if (i.includes("@") && i[0] !== "@"){
                        this.complete.push({"mail": i})
                    }else if (i.includes("www.")){
                        this.complete.push({"link": i})
                    }else{
                        this.complete.push({"text": i})
                    }
                });
            }
        }
    }
</script>
