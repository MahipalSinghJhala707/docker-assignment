const express = require("express");
const fetch = require("node-fetch");

const app = express();

app.use(express.urlencoded({ extended: true }));
app.use(express.static("public"));

app.post("/submit", async (req, res) => {
  const response = await fetch("http://backend:5000/submit", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(req.body)
  });

  const data = await response.json();
  res.send(`<h2>Response from Flask: ${data.message}</h2>`);
});

app.listen(3000, () => {
  console.log("Frontend running on port 3000");
});
