

function SellProduct(product_id){
        
    let city_id = window.location.pathname.split('/')[2];
    
    axios.post(`/SellProduct/${city_id}/${product_id}`)
    .then(()=>{
        location.reload(); 

    })
    
    
    
}

function BuyProduct(product_id){

    let city_id = window.location.pathname.split('/')[2];
    
    axios.post(`/BuyProduct/${city_id}/${product_id}`)
    .then(()=>{
        location.reload(); 
    }) 
   


}

    
