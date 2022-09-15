

function GetDealerData(){
    
    let dealer_id = localStorage.getItem('dealer_id')

    let form_data = new FormData();
    form_data.append( 'dealer_id', dealer_id);

    axios.post(`/GetDealerData/${dealer_id}`)
    .then((response)=>{
        let dealer_money = response.data

        dealer_money = dealer_money.split(' ')

        let dealer_money_text = document.getElementById('dealer_money')
        dealer_money_text.innerText = dealer_money[1] 

        console.log(dealer_money);

    })
}

GetDealerData()

function SellProduct(product_id){
        
    let city_id = window.location.pathname.split('/')[2];
    let dealer_id = localStorage.getItem('dealer_id')

    axios.post(`/SellProduct/${city_id}/${product_id}/${dealer_id}`)
    .then(()=>{
        location.reload(); 

    })
    
    
    
}

function BuyProduct(product_id){

    let city_id = window.location.pathname.split('/')[2];
    let dealer_id = localStorage.getItem('dealer_id')
    
    axios.post(`/BuyProduct/${city_id}/${product_id}/${dealer_id}`)
    .then(()=>{
        location.reload(); 
    }) 
   


}

    
