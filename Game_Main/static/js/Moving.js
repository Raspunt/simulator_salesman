



class TelegaMoving{



    Start() {

        
        let daysid = document.getElementById('days')
        let event_name = document.getElementById('event_name')
        let finish_btn = document.getElementById('FinishBtn')

        let timer = setInterval(()=>{
            days--;
            
            let randomEvent = this.GetRandomEvent()
            
            // console.log(randomEvent[0],randomEvent[1]);
            // console.log(days);

            days += randomEvent[1]
            daysid.innerText = days + "Дней"
            event_name.innerText = randomEvent[0]
            
            
            

            if (days <= 0){
                finish_btn.style.display =" block"
                clearInterval(timer)
            }
            
        },1000)

        


    } 

    GetRandomEvent(){

        let events = [
            ['Обычный день',0],
            ["Дождь",2],
            ["Ровная дорога",-2],
            ["Река",2],
            ["Встретил местного",-3]
        ]

        return events[Math.floor(Math.random()*events.length)];
    }






}


function TravelIsDone(){

    let city_id = window.location.pathname.split('/')[2];

    window.location.href = `/MovingDone/${city_id}`
}




let telega = new TelegaMoving()




telega.Start()
