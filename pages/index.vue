<template>
  <v-row justify="center" align="center" class="w-full h-auto mx-auto p-0">
    <v-col class="w-full h-auto">
      
      <v-card class="py-4 flex-col justify-center rounded-b-none">
        <div class="inline-flex w-full h-auto mx-auto">
          <div class="grid grid-cols-1 grid-rows-1 place-items-center w-10 min-h-full px-3">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M3 0C1.355 0 0 1.355 0 3V17C0 18.645 1.355 20 3 20H17C18.645 20 20 18.645 20 17V3C20 1.355 18.645 0 17 0H3ZM3 2H17C17.571 2 18 2.429 18 3V17C18 17.571 17.571 18 17 18H3C2.429 18 2 17.571 2 17V3C2 2.429 2.429 2 3 2ZM9.984 4.986C9.438 4.995 9 5.439 9 5.986C9 5.991 9 5.996 9 6V5.999V8.999H6C5.996 8.999 5.991 8.999 5.986 8.999C5.434 8.999 4.986 9.447 4.986 9.999C4.986 10.551 5.434 10.999 5.986 10.999C5.991 10.999 5.996 10.999 6.001 10.999H9V13.999C9 14.003 9 14.008 9 14.013C9 14.565 9.448 15.013 10 15.013C10.552 15.013 11 14.565 11 14.013C11 14.008 11 14.003 11 13.998V13.999V10.999H14C14.004 10.999 14.009 10.999 14.014 10.999C14.566 10.999 15.014 10.551 15.014 9.999C15.014 9.447 14.566 8.999 14.014 8.999C14.009 8.999 14.004 8.999 13.999 8.999H11V5.999C11 5.995 11 5.99 11 5.985C11 5.433 10.552 4.985 10 4.985C9.995 4.985 9.989 4.985 9.984 4.985H9.985L9.984 4.986Z" fill="#007FFF"/>
            </svg>
          </div>
          <input type="text" v-model="texto" v-on:keyup.enter="addTask()" placeholder="Type to add new task" class="w-full border-none ring-none pr-3 py-2 px-1 mr-2" />
          <div v-show="texto.length > 0" class="grid grid-cols-1 grid-rows-1 place-items-center w-10 min-h-full px-3 opacity-50">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
              <circle cx="12" cy="12" r="12" fill="url(#pattern0)"/>
              <defs>
              <pattern id="pattern0" patternContentUnits="objectBoundingBox" width="1" height="1">
              <use xlink:href="#image0_1314_758" transform="translate(0 -0.254717) scale(0.0188679)"/>
              </pattern>
              <image id="image0_1314_758" width="53" height="80" xlink:href="data:image/jpeg;base64,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"/>
              </defs>
            </svg>
          </div>
        </div>
      </v-card>

      <v-card v-show="list.length > 0" class="py-4 flex-col justify-center rounded-t-none space-y-2">
        <div v-for="item in list" :key="item.id" class="flex space-x-2 px-2 py-0">
          <input type="checkbox" v-model="item.check" v-bind:id="item.id"><span class="flex content-center" :class="{ 'line-through': item.check}"> <Texto :text="item.text" /> </span>
        </div>
      </v-card>

      <v-card v-show="texto.length > 0" class="py-4 flex-col justify-center rounded-t-none">
        <div class="inline-flex w-full h-auto mx-auto lg:px-4 lg:space-x-2">
          <div class="flex-col">
            <div class="inline-flex space-x-1 pl-2">
              <span class="inline-flex px-3 lg:space-x-3 border-gray-400 rounded-md h-10 lg:px-6 bg-gray-100 place-items-center opacity-50">
                <svg class="place-self-center" width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M13 0C12.996 0 12.991 0 12.986 0C12.434 0 11.986 0.448 11.986 1C11.986 1.552 12.434 2 12.986 2C12.991 2 12.996 2 13.001 2H16.586L11.293 7.293C10.311 8.236 11.765 9.689 12.707 8.707L18 3.414V7C18 7.004 18 7.009 18 7.014C18 7.566 18.448 8.014 19 8.014C19.552 8.014 20 7.566 20 7.014C20 7.009 20 7.004 20 6.999V7V1C20 0.448 19.552 0 19 0H13V0ZM7.97998 10.99C7.71998 10.998 7.47398 11.106 7.29298 11.293L1.99998 16.586V13C1.99998 12.996 1.99998 12.991 1.99998 12.986C1.99998 12.434 1.55198 11.986 0.999977 11.986C0.994977 11.986 0.988977 11.986 0.983977 11.986H0.984977C0.438977 11.995 0.000976562 12.439 0.000976562 12.986C0.000976562 12.991 0.000976562 12.996 0.000976562 13V12.999V18.999C0.000976562 19.551 0.448977 19.999 1.00098 19.999H7.00098C7.00498 19.999 7.00998 19.999 7.01498 19.999C7.56698 19.999 8.01498 19.551 8.01498 18.999C8.01498 18.447 7.56698 17.999 7.01498 17.999C7.00998 17.999 7.00498 17.999 6.99998 17.999H3.41498L8.70798 12.706C9.36198 12.07 8.89298 10.962 7.98098 10.989L7.97998 10.99Z" fill="#4E5D78"/>
                </svg>
                <span v-show="text" class="font-bold w-auto text-sm">Open</span>
              </span>

              <span class="p-1"></span>

              <span class="inline-flex px-3 lg:space-x-3 border-gray-400 border border-opacity-70 rounded-sm lg:px-5 place-items-center opacity-50">
                <svg width="20" height="23" viewBox="0 0 20 23" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M5.984 0.986009C5.438 0.995009 5 1.43901 5 1.98601C5 1.99101 5 1.99601 5 2.00001V1.99901V2.99901H3C1.355 2.99901 0 4.35401 0 5.99901V19.999C0 21.644 1.355 22.999 3 22.999H17C18.645 22.999 20 21.644 20 19.999V5.99901C20 4.35401 18.645 2.99901 17 2.99901H15V1.99901C15 1.99501 15 1.99001 15 1.98501C15 1.43301 14.552 0.985009 14 0.985009C13.995 0.985009 13.989 0.985009 13.984 0.985009H13.985C13.439 0.994009 13.001 1.43801 13.001 1.98501C13.001 1.99001 13.001 1.99501 13.001 1.99901V1.99801V2.99801H7.001V1.99801C7.001 1.99401 7.001 1.98901 7.001 1.98401C7.001 1.43201 6.553 0.984009 6.001 0.984009C5.996 0.984009 5.99 0.984009 5.985 0.984009H5.986L5.984 0.986009ZM3 5.00001H5V6.00001C5 6.00401 5 6.00901 5 6.01401C5 6.56601 5.448 7.01401 6 7.01401C6.552 7.01401 7 6.56601 7 6.01401C7 6.00901 7 6.00401 7 5.99901V6.00001V5.00001H13V6.00001C13 6.00401 13 6.00901 13 6.01401C13 6.56601 13.448 7.01401 14 7.01401C14.552 7.01401 15 6.56601 15 6.01401C15 6.00901 15 6.00401 15 5.99901V6.00001V5.00001H17C17.571 5.00001 18 5.42901 18 6.00001V9.00001H2V6.00001C2 5.42901 2.429 5.00001 3 5.00001V5.00001ZM2 11H18V20C18 20.571 17.571 21 17 21H3C2.429 21 2 20.571 2 20V11Z" fill="#8A94A6"/>
                </svg>
                <span v-show="text" class="font-medium text-sm text-gray-400">Today</span>
              </span>

              <span class="inline-flex px-3 lg:space-x-3 border-gray-400 border border-opacity-70 rounded-sm lg:px-5 place-items-center opacity-50">
                <svg width="20" height="23" viewBox="0 0 20 23" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M10.438 1.01001C10.09 0.985006 9.74098 0.991006 9.39698 1.02601C6.64498 1.30401 3.99698 3.50501 4.00098 7.00301V10.001H3.00098C1.35598 10.001 0.000976562 11.356 0.000976562 13.001V20.001C0.000976562 21.646 1.35598 23.001 3.00098 23.001H17.001C18.646 23.001 20.001 21.646 20.001 20.001V13.001C20.001 11.356 18.646 10.001 17.001 10.001H6.00098V6.99901C5.99798 4.46301 7.69898 3.20801 9.59898 3.01701C11.499 2.82601 13.417 3.71601 13.921 6.20101C14.187 7.50701 16.148 7.10901 15.882 5.80301C15.273 2.80401 12.873 1.18401 10.439 1.01201L10.438 1.01001ZM2.99998 12H17C17.571 12 18 12.429 18 13V20C18 20.571 17.571 21 17 21H2.99998C2.42898 21 1.99998 20.571 1.99998 20V13C1.99998 12.429 2.42898 12 2.99998 12Z" fill="#8A94A6"/>
                </svg>
                <span  v-show="text" class="font-medium text-sm text-gray-400">Public</span>
              </span>

              <span class="inline-flex px-3 lg:space-x-3 border-gray-400 border border-opacity-70 rounded-sm lg:px-5 place-items-center opacity-50">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M11.9841 0.985985C11.4381 0.994985 11.0001 1.43899 11.0001 1.98599C11.0001 1.99099 11.0001 1.99599 11.0001 1.99999V1.99899V5.99899C11.0001 6.00299 11.0001 6.00799 11.0001 6.01299C11.0001 6.56499 11.4481 7.01299 12.0001 7.01299C12.5521 7.01299 13.0001 6.56499 13.0001 6.01299C13.0001 6.00799 13.0001 6.00299 13.0001 5.99799V5.99899V1.99899C13.0001 1.99499 13.0001 1.98999 13.0001 1.98499C13.0001 1.43299 12.5521 0.984985 12.0001 0.984985C11.9951 0.984985 11.9891 0.984985 11.9841 0.984985H11.9851L11.9841 0.985985ZM4.92008 3.91999C4.36808 3.91999 3.92008 4.36799 3.92008 4.91999C3.92008 5.20099 4.03608 5.45499 4.22208 5.63599L7.05208 8.46598C7.23408 8.65598 7.49008 8.77298 7.77308 8.77298C8.32508 8.77298 8.77308 8.32498 8.77308 7.77298C8.77308 7.48998 8.65508 7.23399 8.46608 7.05199L5.63608 4.22199C5.45408 4.03499 5.20008 3.91899 4.91908 3.91899L4.92008 3.91999ZM19.0511 3.91999C18.7811 3.92799 18.5391 4.04299 18.3641 4.22299L15.5341 7.05299C15.3441 7.23499 15.2271 7.49099 15.2271 7.77399C15.2271 8.32599 15.6751 8.77399 16.2271 8.77399C16.5101 8.77399 16.7661 8.65599 16.9481 8.46699L19.7781 5.63699C19.9651 5.45499 20.0811 5.20099 20.0811 4.91999C20.0811 4.36799 19.6331 3.91999 19.0811 3.91999C19.0711 3.91999 19.0601 3.91999 19.0501 3.91999H19.0521H19.0511ZM12.0001 9.99999C10.8951 9.99999 10.0001 10.895 10.0001 12C10.0001 13.105 10.8951 14 12.0001 14C13.1051 14 14.0001 13.105 14.0001 12C14.0001 10.895 13.1051 9.99999 12.0001 9.99999ZM2.00008 11C1.99608 11 1.99108 11 1.98608 11C1.43408 11 0.986084 11.448 0.986084 12C0.986084 12.552 1.43408 13 1.98608 13C1.99108 13 1.99608 13 2.00108 13H6.00008C6.00408 13 6.00908 13 6.01408 13C6.56608 13 7.01408 12.552 7.01408 12C7.01408 11.448 6.56608 11 6.01408 11C6.00908 11 6.00408 11 5.99908 11H2.00008V11ZM18.0001 11C17.9961 11 17.9911 11 17.9861 11C17.4341 11 16.9861 11.448 16.9861 12C16.9861 12.552 17.4341 13 17.9861 13C17.9911 13 17.9961 13 18.0011 13H22.0001C22.0041 13 22.0091 13 22.0141 13C22.5661 13 23.0141 12.552 23.0141 12C23.0141 11.448 22.5661 11 22.0141 11C22.0091 11 22.0041 11 21.9991 11H18.0001ZM7.74008 15.23C7.47008 15.238 7.22808 15.353 7.05308 15.533L4.22308 18.363C4.03308 18.545 3.91608 18.801 3.91608 19.084C3.91608 19.636 4.36408 20.084 4.91608 20.084C5.19908 20.084 5.45508 19.966 5.63708 19.777L8.46708 16.947C8.65408 16.765 8.77008 16.511 8.77008 16.23C8.77008 15.678 8.32208 15.23 7.77008 15.23C7.76008 15.23 7.74908 15.23 7.73908 15.23H7.74108H7.74008ZM16.2301 15.23C15.6781 15.23 15.2301 15.678 15.2301 16.23C15.2301 16.511 15.3461 16.765 15.5321 16.946L18.3621 19.776C18.5441 19.966 18.8001 20.083 19.0831 20.083C19.6351 20.083 20.0831 19.635 20.0831 19.083C20.0831 18.8 19.9651 18.544 19.7761 18.362L16.9461 15.532C16.7641 15.345 16.5101 15.229 16.2291 15.229L16.2301 15.23ZM11.9841 16.986C11.4381 16.995 11.0001 17.439 11.0001 17.986C11.0001 17.991 11.0001 17.996 11.0001 18V17.999V21.999C11.0001 22.003 11.0001 22.008 11.0001 22.013C11.0001 22.565 11.4481 23.013 12.0001 23.013C12.5521 23.013 13.0001 22.565 13.0001 22.013C13.0001 22.008 13.0001 22.003 13.0001 21.998V21.999V17.999C13.0001 17.995 13.0001 17.99 13.0001 17.985C13.0001 17.433 12.5521 16.985 12.0001 16.985C11.9951 16.985 11.9891 16.985 11.9841 16.985H11.9851L11.9841 16.986Z" fill="#8A94A6"/>
                </svg>
                <span v-show="text" class="font-medium text-sm text-gray-400">Highlight</span>
              </span>

              <span class="inline-flex px-3 lg:space-x-3 border-gray-400 border border-opacity-70 rounded-sm lg:px-5 place-items-center opacity-50">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M12 0C5.38443 0 0 5.38443 0 12C0 18.6156 5.38443 24 12 24C18.6156 24 24 18.6156 24 12C24 5.38443 18.6156 0 12 0ZM12 2C17.5347 2 22 6.46531 22 12C22 17.5347 17.5347 22 12 22C6.46531 22 2 17.5347 2 12C2 6.46531 6.46531 2 12 2ZM12.1816 7C11.1076 7 10.3071 7.34918 9.78125 8.04883C9.25986 8.74847 9 9.79794 9 11.1973V12.8828C9.01337 14.2419 9.2861 15.2696 9.81641 15.9648C10.3512 16.6555 11.1436 17 12.1953 17C13.2648 17 14.0606 16.646 14.582 15.9375C15.1078 15.2245 15.3711 14.1688 15.3711 12.7695V11.084C15.3578 9.72482 15.0863 8.70526 14.5605 8.02344C14.0391 7.34162 13.2467 7 12.1816 7ZM12.1816 8.30273C12.7253 8.30273 13.1215 8.5175 13.3711 8.94531C13.6206 9.36866 13.7461 10.0377 13.7461 10.9512V13.1504C13.7327 14.0283 13.6012 14.6735 13.3516 15.0879C13.102 15.4979 12.7167 15.7031 12.1953 15.7031C11.6516 15.7031 11.252 15.4808 10.998 15.0352C10.744 14.5895 10.6172 13.9111 10.6172 13.002V10.7969C10.6306 9.94125 10.7622 9.31318 11.0117 8.91211C11.2613 8.50659 11.6513 8.30273 12.1816 8.30273Z" fill="#8A94A6"/>
                </svg>
                <span v-show="text" class="font-medium text-sm text-gray-400">Estimation</span>
              </span>
            </div>
          </div>
          <div class="w-full flex-col justify-items-center">
            <div class="flex justify-end space-x-1 font-medium pr-1">
              <button v-show="text" href="" class="border-gray-500 rounded-md py-2 px-4 bg-gray-300 text-black">Cancel</button>
              <button v-show="!write" href="" class="border-gray-500 rounded-md py-2 px-4 bg-blue-800 text-white">Ok</button>
              <button v-show="write && text" href="" @click="addTask()" class="border-gray-500 rounded-md py-2 px-4 bg-blue-800 text-white">Add</button>
              <button v-show="!text" href="" @click="addTask()" class="rounded-md py-2 px-4 bg-blue-800 text-white">
                <svg width="24" height="24" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M3 0C1.355 0 0 1.355 0 3V17C0 18.645 1.355 20 3 20H17C18.645 20 20 18.645 20 17V6C20 5.735 19.895 5.48 19.707 5.293L14.707 0.293C14.519 0.105 14.265 0 14 0H3ZM3 2H4V6C4 6.552 4.448 7 5 7H13C14.352 7.019 14.352 4.981 13 5H6V2H13.586L18 6.414V17C18 17.564 17.564 18 17 18H16V11C16 10.448 15.552 10 15 10H5C4.448 10 4 10.448 4 11V18H3C2.436 18 2 17.564 2 17V3C2 2.436 2.436 2 3 2ZM6 12H14V18H6V12Z" fill="white"/>
                </svg>
              </button>
            </div>
          </div>
        </div>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import Texto from '~/components/texto.vue';
// import nuxtConfig from '~/nuxt.config';

const axios = require('axios');

export default {
    name: "IndexPage",
    data() {
        return {
            write: true,
            list: [],
            texto: "",
        };
    },
    async mounted() {
        await this.initialize();
    },
    computed: {
        text() {
            return this.$breakpoints.lLg;
        }
    },
    methods: {
        async initialize() {
            this.list = [];
            await axios.get("http://localhost:8000/notes/")
                .then((response) => {
                response.data.forEach(item => {
                    this.list.push({
                        "id": item.id,
                        "check": item.hecho,
                        "text": item.content
                    });
                });
            })
                .catch((error) => {
                console.error(error);
            });
        },
        async addTask() {
            await axios.post("http://localhost:8000/notes/", {
                "content": this.texto,
                "hecho": false
            })
                .then((response) => {
                console.log(response);
            })
                .catch((error) => {
                console.error(error);
            });
            // const id = this.list.length
            // this.list.push({id, check: false, text: this.texto})
            this.texto = "";
            await this.initialize();
        },
    },
    components: { Texto }
}
</script>
