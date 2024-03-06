import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient()
      .on('error', (err) => console.log(`Something went wrong with Redis Server: ${err}`))
      .on('connect', () => console.log('Redis Server is connedted'));

const listProducts = [
    { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
    { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
    { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
    { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 }
];

function getItemById(id) {
    for (const product of listProducts) {
	if (product.itemId === id) return product;
    }
}

function reserveStockById(itemId, stock) {
    // const productInfo = getItemById(id)
    client.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
    const get = promisify(client.get).bind(client);
    const stock = await get(`item.${itemId}`);
    return stock;
}

const HOST = 'localhost';
const PORT = 1245;
const app = express();
app.use(express.json());

app.get('/list_products', (req, res) => {
    res.status(200).json(listProducts);
});

app.get('/list_products/:itemId([0-9]+)', async (req, res) => {
    const id = Number(req.params.itemId);
    const product = getItemById(id);
    if (product) {
	product.currentQuantity = await getCurrentReservedStockById(id)
	res.status(200).json(product);
    } else {
	res.status(200).json({"status":"Product not found"});
    }
});

app.get('/reserve_product/:itemId([0-9]+)', (req, res) => {
    const id = Number(req.params.itemId);
    const product = getItemById(id);
    if (!product) {
	res.status(200).json({"status":"Product not found"});
    } else {
	if (product >= 1)
	    res.status(200).json({"status":"Reservation confirmed","itemId":id});
	else {
	    res.status(200).json({"status":"Not enough stock available","itemId":id});
	}
    }
});

app.listen(PORT, HOST, () => {
    console.log(`App is running on ${PORT}...`);
});
