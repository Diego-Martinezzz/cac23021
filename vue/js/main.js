const { createApp } = Vue
createApp({
    data() {
      return {
        message: 'Hello Vue!',
        nombre: 'Juancito',
        apellido: 'Dominguez',
        error: 'true',
        imagen: "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANQAAAB3CAMAAABMiJ5qAAAAw1BMVEUKY/n///////0KZPj8//z///v8//8AYvoKZPYAX/n///kAW/gAXvsAYPwAVvQAWfcATfEAUfIAT+wAWfHy+Pf19/pZhO+uyPAAW90ydeVMhexvmfR5ofBSlvMZZPAwb+eSsOS/1e/c7/lBeu6kuunK3vLT4/IzbO2PsvDs8foUWL8ASNVRhPVije4AUOeBpOFxmdiDoumdv+uuy+tlkOHC0vNajOYAOuZymeFdguIAV+d2l+pKePQ4fOeWu+59reUQXtcB5o8EAAAGP0lEQVR4nN2c/VviOBDHm2nS0BdaSouIei1FaO3dooeIq+ju3f//V10i4LrrC03W0ul9nwd/UpsPM5lMJpMahmEahtGRPw4i0+Dc9tzANUz5TLOWB5vbz0HE7SAI+8ejk9OzP7i5fXgdTz8UkckDO0lPx9",
        encabezado: "<h1>Clase de Vue</h1>",
        frutas: ['naranja','banana','durazno'],
        fotos:[
            "https://rickandmortyapi.com/api/character/avatar/1.jpeg",
            "https://rickandmortyapi.com/api/character/avatar/2.jpeg",
            "https://rickandmortyapi.com/api/character/avatar/3.jpeg",
            "https://rickandmortyapi.com/api/character/avatar/4.jpeg",
            "https://rickandmortyapi.com/api/character/avatar/5.jpeg",
            "https://rickandmortyapi.com/api/character/avatar/6.jpeg",
            ],
        personajes: [
                {
                "id": 1,
                "name": "Rick Sanchez",
                "status": "Alive",
                "species": "Human",
                "type": "",
                "gender": "Male",
                "image": "https://rickandmortyapi.com/api/character/avatar/1.jpeg",
                "created": "2017-11-04T18:48:46.250Z"
                },
            ],
        personajes: [
                {
                "id": 1,
                "name": "Pedro perez",
                "status": "Alive",
                "species": "Gato",
                "type": "",
                "gender": "Male",
                "image": "https://rickandmortyapi.com/api/character/avatar/2.jpeg",
                "created": "2017-11-04T18:48:46.250Z"
                },
            ]
      }
    }
  }).mount('#app')