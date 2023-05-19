const {createApp} = Vue

createApp({
    data(){
        return{
            frutas:[
                {"fruta": "banana", "stock": 15},
                {"fruta": "manzana", "stock": 20},
                {"fruta": "pera", "stock": 300}

            ]
        }
    }
}).mount('#app1')