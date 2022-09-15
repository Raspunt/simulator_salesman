



class TelegaMoving{



    Start(events) {

        
        let daysid = document.getElementById('days')
        let event_name = document.getElementById('event_name')
        let finish_btn = document.getElementById('FinishBtn')

        let history_of_events = []

        let timer = setInterval(()=>{
            days--;
            
            let randomEvent = this.GetRandomEvent(events)
            

            console.log(randomEvent);

            if (randomEvent[1] != undefined){
   
                days += parseInt(randomEvent[1])
                // console.log( parseInt(randomEvent[1]))

                daysid.innerText = days + "Дней"
                event_name.innerText = randomEvent[0]
                history_of_events.push(randomEvent[0])
                
            }
            
        
            if (days <= 0){
                finish_btn.style.display =" block"
                clearInterval(timer)

                localStorage.setItem("historyOfEvents",history_of_events)

            }
            
        },100)

        


    } 


    GetRandomEvent(events){

        return events[Math.floor(Math.random()*events.length)];
    }


    GetAllEvents(callback){

        axios.get(`/GetEvents/`)
        .then((response)=>{
             
            let events = response.data.split("^")
            
            let eventsD = []

            for (let i = 0 ; i < events.length;i++){
                
                let eventName = events[i].split("*")[0]
                let event_days = events[i].split("*")[1]

                eventsD.push([eventName,event_days])
            }
            console.log(eventsD);
            
            callback(eventsD)
                
        })


    }

     removeObjectWithId(arr, id) {
        const objWithIdIndex = arr.findIndex((obj) => obj.id === id);
        arr.splice(objWithIdIndex, 1);
      
        return arr;
      }






}


function TravelIsDone(){

    let city_id = window.location.pathname.split('/')[2];

    window.location.href = `/MovingDone/${city_id}`
}




let telega = new TelegaMoving()



telega.GetAllEvents((rez)=>{
    telega.Start(rez)

})
