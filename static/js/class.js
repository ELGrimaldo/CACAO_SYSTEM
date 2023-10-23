Dropzone.autoDiscover = false;

const myDropzone = new Dropzone("#my-awesome-dropzone", {
    url: "connection/",
    maxFiles: 100,
    maxFilesize: 2,
    acceptedFiles: '.png, .jpg'
})

console.log("Working Drop Zone")