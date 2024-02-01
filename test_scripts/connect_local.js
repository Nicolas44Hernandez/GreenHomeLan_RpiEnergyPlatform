const { MongoClient } = require("mongodb");
 
// Replace the following with your Atlas connection string                                                                                                                                        
//const url = "mongodb+srv://n44hernandezp:WiGreen2024@cluster0.ydgbl9o.mongodb.net/?retryWrites=true&w=majority";
const url = "mongodb://0.0.0.0:27017";

// Connect to your Atlas cluster
const client = new MongoClient(url);

async function run() {
    try {
        await client.connect();
        console.log("Successfully connected to Local");

    } catch (err) {
        console.log(err.stack);
    }
    finally {
        await client.close();
    }
}

run().catch(console.dir);