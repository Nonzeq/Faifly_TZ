import { set } from "mobx";
import React, { useEffect, useState } from "react";
import WorkerAppointmentItem from "../components/workerAppointmentItem";
import { useFetching } from "../hooks/useFetching";
import $api from "../http";
import Mybutton from "../UI/buttons/MyButton";
import Myinput from "../UI/inputs/MyInput";
import Myloader from "../UI/Loader/ Myloader";

const WorkerAppointment = () => {
  useEffect(() => {
    getUserAppointment();
  }, []);
  const [appointment, setAppointment] = useState([]);
  const [date, setDate] = useState("")
  const [non, setNon] = useState(true)



  const [getUserAppointment, isLoading, isErorr] = useFetching(async () => {
    try {
      const response = await $api.get(
        `http://127.0.0.1:8000/api/worker/AppointmentList/?worker=${localStorage.getItem('worker_id')}`
      );
      setAppointment(response.data);
    } catch (e) {
      console.log(e.response.data);
    }
  })


  const getUserAppointmentDayFilter = async () => {
    try {
      const response = await $api.get(
        `http://127.0.0.1:8000/api/worker/AppointmentList/?worker=${localStorage.getItem('worker_id')}&date=${date}`
      );
      setAppointment(response.data);
      
      if(response.data[0] == null){
        setNon(false)
        console.log(response.data);
      }else{
        setNon(true)
      }
    } catch (e) {
      console.log(e.response.data);
    }
  };
  if(!non){
    return(

      <div>
        <div className="appointment__wrapper">  
      <h2>Appointment for me</h2></div>
  <div className="appointment__wrapper">   
    <div className="post">
      
      <div className="post__content">
        <div key={Date.now()} className="groups">
        <div className="appointment__wrapper">  
          <Myinput onChange={(e) => setDate(e.target.value)}
              value={date}
              type="date"
              placeholder="date"
          ></Myinput>
          <Mybutton onClick={() => getUserAppointmentDayFilter()}>Filter</Mybutton>
          </div>
          
        </div>
      </div>
    </div>
  </div>
  <div className="appointment__wrapper">
    <h3>No any appointment on this date</h3>
    </div>
  </div>
    )
  }

  return (

    <div className="appointment_content">
      <div className="appointment__wrapper">  
        <h2>Appointment for me</h2></div>
    <div className="appointment__wrapper">   
      <div className="post">
        
        <div className="post__content">
          <div key={Date.now()} className="groups">
          <div className="appointment__wrapper">  
            <Myinput onChange={(e) => setDate(e.target.value)}
                value={date}
                type="date"
                placeholder="date"
            ></Myinput>
            <Mybutton onClick={() => getUserAppointmentDayFilter()}>Filter</Mybutton>
            </div>
            
            {/* {appointment.map((app) => (
              <p>
                <strong>Date: </strong>{app.date}|
                <strong>apointment_start: </strong>
                  {app.apointment_start} | 
                  <strong>apointment_end:</strong>
                  {app.apointment_end}|

                <strong> user: </strong>
                {app.user}
              </p>
            ))} */}
        

            
          </div>
          
        </div>
        
      </div>
      
    </div>
      {isLoading
      ?<div className='appointment__wrapper'><div className="loaderError__container"><Myloader /></div></div>
      :<WorkerAppointmentItem appointment={appointment}/>
      }
    </div>
  );
};

export default WorkerAppointment;
