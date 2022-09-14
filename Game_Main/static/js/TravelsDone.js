

function SellProduct(product_id){

    const city_id = localStorage.getItem('city_id');


    axios.post('/SellProduct/', {
        city_id: city_id,
        product_id: product_id
    })

    console.log("Продаем продукты");

}