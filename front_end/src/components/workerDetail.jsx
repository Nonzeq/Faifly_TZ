import axios from "axios";
import { observer } from "mobx-react-lite";
import React from "react";
import { useEffect } from "react";
import { useState } from "react";
import { useParams } from "react-router-dom";
import ErrorBoundary from "../error/errorBoundary";
import Mybutton from "../UI/buttons/MyButton";
import Mymodal from "../UI/modal/myModal";
import AppointForm from "./AppointForm";
import AppointmentList from "./appointmentList";

function WorkerDetail() {
  const days = [
    { id: 1, title: "Monday" },
    { id: 2, title: "TUESDAY" },
    { id: 3, title: "WEDNESDAY" },
    { id: 4, title: "THURSDAY" },
    { id: 5, title: "FRIDAY" },
    { id: 6, title: "SATURDAY" },
    { id: 7, title: "SUNDAY" },
  ];
  const { workerId } = useParams();

  useEffect(() => {
    getWorkerById();
  }, []);
  const [modal, setModal] = useState(false);
  const [worker, getWorker] = useState([]);
  const [sheldule, getSheldule] = useState([]);
  const [day, setDay] = useState("");

   const off_modal = () => {
    setModal(false)
  }
  const getWorkerById = async () => {
    const res = await axios.get(
      `http://127.0.0.1:8000/api/client/worker/?id=${workerId}`
    );
    getWorker(res.data);
  };
  const getScheduleByDay = async () => {
    const res = await axios.get(
      `http://127.0.0.1:8000/api/client/SchelduleList/?work_day=${day}&worker=${workerId}`
    );
    getSheldule(res.data);
    console.log(res.data);
  };

  return (
    
    <div className="group__wrapper">
      <div className="post__appoint_content">
        {worker.map((worker) => (
          <h3>Shedule for {worker.full_name}</h3>
        ))}
        <select
          style={{ margin: "20px 20px" }}
          value={day}
          onChange={(e) => setDay(e.target.value)}
        >
          <option key={sheldule.id}>Take shedule</option>
          {days.map((p) => (
            <option key={p.id} value={p.title}>
              {p.title}
            </option>
          ))}
        </select>
        <Mybutton onClick={() => getScheduleByDay()}>Get Shedule</Mybutton>

        {sheldule.map((sh) => (
          <p>
            {/* <h3>{sh.work_day}</h3> */}
            <strong>Day:</strong> {sh.work_day}<br/>
           <strong>Work time:</strong> {sh.time_start}-{sh.time_end}
          </p>
        ))}
          
          
      </div>
      <div className="post__appoint_content">
      <AppointmentList workerId={workerId}/>
     
      </div>
      <div className="post__appoint_content">       
      <Mybutton  onClick={() => setModal(true)}>Add Appointment</Mybutton></div>
      <Mymodal visible={modal} setVisible={setModal}><AppointForm off_modal={off_modal} workerId={workerId}/></Mymodal>
      
    </div>
    
  );
}

export default observer(WorkerDetail);
