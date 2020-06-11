
const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const db = require("./db");
const controller = require("./controllers");

const server = express();

const origin = { origin: '*', }
server.use(cors(origin));

server.use(bodyParser.urlencoded({ extended: false }));
server.use(bodyParser.json());


server.get("/edwj-today", controller.get_today);

server.post("/add-today", controller.add_today);



db.sync()
  .then(() => {
    server.listen(3030, () => {
      console.log(`up on :3030`);
    })
  })
  .catch(error => { throw error; })