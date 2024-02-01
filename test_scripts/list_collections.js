const { MongoClient } = require("mongodb");

// Replace the uri string with your connection string.
//const uri = "mongodb+srv://n44hernandezp:WiGreen2024@cluster0.ydgbl9o.mongodb.net/?retryWrites=true&w=majority";
//const uri = "mongodb://api:docker1234@mongo";
//const uri = "mongodb://0.0.0.0:27017/bezkoder_db";
const uri = "mongodb://tal:tal@0.0.0.0:27017";

const client = new MongoClient(uri);

async function run() {
  try {

    await client.connect();
    const database = client.db("database");
    const collections = await database.listCollections().toArray();
    console.log(collections);
  } finally {
    // Ensures that the client will close when you finish/error
    await client.close();
  }
}
run().catch(console.dir);