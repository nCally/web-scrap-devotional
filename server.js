
const express = require("express");
const cors = require("cors");
const db = require("./db");

const server = express();

const origin = { origin: '*', }
server.use(cors(origin));




server.get("/edwj-today");



db.sync()
  .then(() => {
    server.listen(3030, () => {
      console.log(`up on :3030`);
    })
  })
  .catch(error => { throw error; })