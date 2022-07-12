import axios from 'axios';

export const API_URL = "http://127.0.0.1:8000"

const $api = axios.create({
    withCredentials:true,
    baseURL:API_URL,
})



$api.interceptors.request.use((config) =>{
    config.headers.Authorization = `Bearer ${localStorage.getItem('tokenAccess')}`
    return config 
})

$api.interceptors.response.use((config) =>{
    return config
}, async (error) => {
    const originalRequest = error.config;
    // console.log(error);
    
    if(error.response.status === 401){
        try{
            const response = await axios.post(`${API_URL}/auth/login/refresh/`,{
                refresh: localStorage.getItem('tokenRefresh'),
                username:localStorage.getItem('email'),
                role:localStorage.getItem('role')
            })
            localStorage.setItem('tokenAccess', response.data.access)
            return $api.request(originalRequest);
        }catch(e){
        //    console.log(e);
        }

    }
    return Promise.reject(error)
})

export default $api;