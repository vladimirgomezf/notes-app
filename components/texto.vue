<template>
    <div class="space-y-2 flex-col items-center">
        <div class="inline-flex" v-for="item in complete" :key="item">
        <!-- {{Object.values(item)[0]}} -->
            <!-- <a href="" class="bg-violet-400 rounded-2xl p-1">{{Object.entries(item)[0][0]}}</a> -->
            <span v-if="Object.entries(item)[0][0] === 'tag'" class="bg-violet-400 rounded-full px-3 bg-opacity-50 text-violet-500 font-bold text-sm pl-1 inline-flex items-center">{{Object.values(item)[0]}}</span>
            <a v-bind:href="'http://twitter.com/'+Object.values(item)[0]" target="_blank" v-if="Object.entries(item)[0][0] === 'people'" class="bg-green-300 rounded-full px-3 bg-opacity-50 inline-flex items-center">
                <!--  -->
                <img class="pr-1 w-6 h-5" src="person.png" />
                <span class="text-green-500 font-bold text-sm pl-1">Natasha</span>
            </a>
            <a v-bind:href="'mailto:'+Object.values(item)[0].trim()" target="_blank" v-if="Object.entries(item)[0][0] === 'mail'" class="bg-orange-300 rounded-full px-3 bg-opacity-50 inline-flex items-center">
                <svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M2.66663 0C1.56996 0 0.666626 0.903333 0.666626 2V10C0.666626 11.0967 1.56996 12 2.66663 12H13.3333C14.43 12 15.3333 11.0967 15.3333 10V2C15.3333 0.903333 14.43 0 13.3333 0H2.66663ZM2.66663 1.33333H13.3333C13.596 1.33333 13.8153 1.48667 13.9246 1.706L7.99996 5.85333L2.07529 1.706C2.18396 1.48733 2.40396 1.33333 2.66663 1.33333ZM1.99996 3.28L7.61729 7.212C7.84729 7.37333 8.15329 7.37333 8.38263 7.212L14 3.28V10C14 10.37 13.7033 10.6667 13.3333 10.6667H2.66663C2.29663 10.6667 1.99996 10.37 1.99996 10V3.28Z" fill="#F58E0A"/>
                </svg>
                <span class="text-orange-500 font-bold text-sm pl-1">Mail</span>
            </a>
            <a v-bind:href="'http://'+Object.values(item)[0].trim()" target="_blank" v-if="Object.entries(item)[0][0] === 'link'" class="bg-sky-300 rounded-full px-3 bg-opacity-50 inline-flex items-center">
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M11.1314 0.658718C10.2367 0.696051 9.30803 1.06872 8.51669 1.83338C8.51536 1.83472 8.51336 1.83738 8.51136 1.84005L8.51069 1.84138L7.36336 2.98072C7.23603 3.10205 7.15736 3.27338 7.15736 3.46272C7.15736 3.83072 7.45603 4.12938 7.82403 4.12938C8.01203 4.12938 8.18203 4.05138 8.30336 3.92605L9.44269 2.79338L9.44669 2.79072C10.1114 2.15005 10.7807 1.95138 11.4247 1.99405C12.07 2.03605 12.7027 2.34805 13.1814 2.82605C13.66 3.30405 13.9714 3.93738 14.0134 4.58272C14.0554 5.22672 13.8567 5.89538 13.2167 6.56072C13.2154 6.56205 13.2154 6.56338 13.214 6.56472L11.222 8.55538V8.55605V8.55672C10.0654 9.71405 8.18136 9.57805 7.20136 8.26738C7.07869 8.10405 6.88536 8.00005 6.66736 8.00005C6.29936 8.00005 6.00069 8.29872 6.00069 8.66672C6.00069 8.81738 6.05069 8.95672 6.13536 9.06805L6.13403 9.06605C7.58603 11.0074 10.4527 11.2114 12.1667 9.49672L14.1667 7.49805C14.1687 7.49605 14.1714 7.49272 14.1734 7.49005L14.174 7.48938C15.048 6.58472 15.4107 5.50205 15.3447 4.49472C15.2787 3.48738 14.8114 2.56938 14.1247 1.88272C13.438 1.19605 12.52 0.728718 11.5127 0.662718C11.3867 0.654718 11.26 0.653384 11.1327 0.658718H11.1314ZM6.53136 5.33872C5.55536 5.36938 4.58469 5.75272 3.83469 6.50272L1.83469 8.50138C1.83269 8.50338 1.83003 8.50672 1.82803 8.50938L1.82736 8.51005C0.95336 9.41472 0.590693 10.4974 0.656693 11.5047C0.722693 12.5121 1.19003 13.4301 1.87669 14.1167C2.56336 14.8034 3.48136 15.2707 4.48869 15.3367C5.49603 15.4027 6.57869 15.0401 7.48336 14.1661C7.48536 14.1641 7.48803 14.1607 7.49003 14.1581L7.49069 14.1574L8.63136 13.0181C8.75803 12.8967 8.83603 12.7261 8.83603 12.5374C8.83603 12.1694 8.53736 11.8707 8.16936 11.8707C7.98069 11.8707 7.81003 11.9494 7.68869 12.0754L6.55336 13.2094C5.88869 13.8501 5.21936 14.0487 4.57536 14.0061C3.93003 13.9641 3.29736 13.6521 2.81869 13.1741C2.34003 12.6961 2.02869 12.0627 1.98669 11.4174C1.94469 10.7734 2.14336 10.1047 2.78336 9.43938C2.78469 9.43805 2.78469 9.43672 2.78603 9.43538L4.77803 7.44472V7.44405V7.44338C5.93469 6.28605 7.81869 6.42205 8.79869 7.73272C8.92136 7.89538 9.11469 8.00005 9.33269 8.00005C9.70069 8.00005 9.99936 7.70138 9.99936 7.33338C9.99936 7.18272 9.94936 7.04338 9.86536 6.93205L9.86669 6.93405C9.14069 5.96338 8.06069 5.42672 6.94869 5.34672C6.80936 5.33672 6.67003 5.33472 6.53069 5.33872H6.53136Z" fill="#007FFF"/>
                </svg>
                <span class="text-blue-500 font-bold text-sm pl-1">Link</span>
            </a>
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
