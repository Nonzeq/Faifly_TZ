import { observer } from "mobx-react-lite";
import React, { useState } from "react";
import $api, { API_URL } from "../http";
import Mybutton from "../UI/buttons/MyButton";
import Myinput from "../UI/inputs/MyInput";

const AppointmentList = (props) => {
  const [appointment, Setappointment] = useState([]);
  const [error, Seterror] = useState(null);
  const [startDate, setStartDate] = useState("");
  // const [valueStart, onChangeStart] = useState("10:00");
  // const [valueEnd, onChangeEnd] = useState("10:00");

  async function getAppointment() {
    try {
      const responce = await $api.get(
        `${API_URL}/api/worker/AppointmentList/?worker=${props.workerId}&date=${startDate}`
      );
      Setappointment(responce.data);
    } catch (e) {
      console.log(e);
    }
  }

  return (
    <div>
      <h3>All Appointment on date</h3>
      <Myinput
        onChange={(e) => setStartDate(e.target.value)}
        value={startDate}
        type="date"
        placeholder="date"
      />
      {appointment.map((appoint) => (
        <p>
          <h3> Date: {appoint.date}</h3>
          Time: {appoint.apointment_start}-{appoint.apointment_end}<br></br>
          Worker: {appoint.user}
        </p>
      ))}
      <Mybutton onClick={() => getAppointment()}>Get all appointment</Mybutton>
    </div>
  );
};

export default observer(AppointmentList);
