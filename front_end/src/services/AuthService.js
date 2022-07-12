import axios from "axios";
import $api from "../http";

export default class AuthService {
    static async login(email, password){
        return $api.post('/auth/login/', {email, password})

    }
    static async registration(username, email, password,password2,role){
        return axios.post('http://127.0.0.1:8000/auth/register/', {username, email, password,password2,role})
        
    }
    static async logout(refresh){
        return $api.post('/auth/logout/',{refresh})
        
    }
    // static async addAppointment(apointment_worker,date,apointment_start,apointment_end){
    //     return $api.post('/api/client/AddAppointment/',{apointment_worker,date,apointment_start,apointment_end})
        
    // }
    
}