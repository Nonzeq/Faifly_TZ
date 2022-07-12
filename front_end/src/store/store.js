
import axios from "axios";
import {makeAutoObservable} from "mobx";
import { API_URL } from "../http";
import AuthService from "../services/AuthService";

export default class Store {
    user = {} 
    isAuth = false
    isLoading = false
    userRole = null
    constructor(){

        makeAutoObservable(this)
    }
    setAuth(bool){
        this.isAuth = bool;
    }
    setUser(user){
        this.user = user;

    }
    setRole(role){
        this.userRole = role
    }
    setLoagind(bool){
        this.isLoading = bool
    }
    async login(email, password){
        try{
            const responce = await AuthService.login(email, password)
            // console.log(responce)
            localStorage.setItem('tokenAccess', responce.data.access)
            localStorage.setItem('tokenRefresh', responce.data.refresh)
            localStorage.setItem('email', responce.data.email)
            localStorage.setItem('id', responce.data.id)
            localStorage.setItem('role', responce.data.role)
            localStorage.setItem('worker_id', responce.data.worker_id)
            this.setAuth(true)
            this.setUser(responce.data.id)
            this.setRole(responce.data.role)
        }catch(e){
                // console.log(e.responce?.data?.message);
                return Promise.reject(e)
        }
    }
    async registration(username, email, password,password2,role){
        try{
            const responce = await AuthService.registration(username, email, password,password2,role)
            // console.log("REGISTER",responce)
            // localStorage.setItem('tokenAccess', responce.data.access)
            // localStorage.setItem('tokenRefresh', responce.data.refresh)
            localStorage.setItem('email', responce.data.email)
            localStorage.setItem('id', responce.data.id)
            localStorage.setItem('role', responce.data.role)
            this.setAuth(true)
            this.setUser(responce.data.id)
            this.setRole(responce.data.role)
        }catch(e){
                // console.log(e);
                return Promise.reject(e)
        }finally{
            this.login(email, password)
            
        }
    }
    async logout(){
        try{
            const responce = await AuthService.logout(localStorage.getItem('tokenRefresh'));
            localStorage.removeItem('tokenAccess');
            localStorage.removeItem('tokenRefresh');
            localStorage.removeItem('username')
            localStorage.removeItem('email')
            localStorage.removeItem('id')
            localStorage.removeItem('role')
            this.setAuth(false)
            this.setUser({})
            this.setRole(null)
        }catch(e){
                console.log(e.response?.data?.message,"ERRROR");
        }
    }
    async checkAuth(){
        this.setLoagind(true)
        try{
            const responce = await axios.post(`${API_URL}/auth/login/refresh/`,{
                refresh: localStorage.getItem('tokenRefresh'),
                username:localStorage.getItem('email'),
                role:localStorage.getItem('role')
            })
            // console.log(responce);
            localStorage.setItem('tokenAccess', responce.data.access)
            this.setAuth(true)
            this.setUser(responce.data.id)
            this.setRole(responce.data.role)
        }catch(e){
            console.log(e.responce?.data?.message);
        }finally{
            this.setLoagind(false)
        }
    }

}