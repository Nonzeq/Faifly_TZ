import Myinput from "../UI/inputs/MyInput";
import React, { useContext, useState } from "react";
import "react-datepicker/dist/react-datepicker.css";
import Mybutton from "../UI/buttons/MyButton";
import { Context } from "..";
import $api from "../http";
import Mymodal from "../UI/modal/myModal";
import WorkerDetail from "./workerDetail";
import { observer } from "mobx-react-lite";

function AppointForm({off_modal,workerId}) {
  const [startDate, setStartDate] = useState("");
  const [valueStart, onChangeStart] = useState("10:00");
  const [valueEnd, onChangeEnd] = useState("10:00");
  const { store } = useContext(Context);
  const[error, setError] = useState(null)



  const addAppointment = async() =>{
      const res = await $api.post('http://127.0.0.1:8000/api/client/AddAppointment/',{
          withCredentials:true,
          apointment_worker:workerId,
          date:startDate,
          apointment_start:valueStart,
          apointment_end:valueEnd,
      }).then(res => (res)).catch(e => setError(e.response.data))
      
      if(res.status == 201){
        off_modal()
        setError('')
      }
  }


  // const addAppointment = async () =>{
  //   try{
  //     const res = await $api.post('http://127.0.0.1:8000/api/client/AddAppointment/',{
  //         withCredentials:true,
  //         apointment_worker:workerId,
  //         date:startDate,
  //         apointment_start:valueStart,
  //         apointment_end:valueEnd,
  //     })
  //   }catch(e){
  //       setError(e.response.data)
  //   }
    
  // }

//   setError(e.response.data.date)
  return (
    <div>
      <form>
      {error && <div style={{color:'red'}}>{error.date || error[0]}</div>}
        <strong>Date:</strong>
        <Myinput
          onChange={(e) => setStartDate(e.target.value)}
          value={startDate}
          type="date"
          placeholder="date"
        />
        <strong>Time start:</strong>
        <Myinput
          onChange={(e) => onChangeStart(e.target.value)}
          value={valueStart}
          type="time"
          placeholder="date"
        />
        <strong>Time end:</strong>
        <Myinput
          onChange={(e) => onChangeEnd(e.target.value)}
          value={valueEnd}
          type="time"
          placeholder="date"
        />
        {/* <strong>Time start :</strong><TimePicker onChange={onChangeStart} value={valueStart} />
            <strong>Time end :</strong><TimePicker onChange={onChangeEnd} value={valueEnd} />
            <h1>{props.workerId}</h1> */}
      </form>
      <Mybutton
        onClick={() =>
            addAppointment()
        }
      >
        Add
      </Mybutton>

    </div>
  );
}

export default observer(AppointForm);
