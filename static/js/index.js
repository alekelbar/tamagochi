const socket = io();

socket.on("url", (url) => {
  $("#imageUrl").attr("src", url);
});

$("#btn-jugar").on("click", (e) => {
  socket.emit("action", "juguemos");
});

$("#btn-alimentar").on("click", (e) => {
  socket.emit("action", "come");
});

$("#btn-dormir").on("click", (e) => {
  socket.emit("action", "duerme");
});

$("#btn-como").on("click", (e) => {
  socket.emit("action", "cómo estás");
});
