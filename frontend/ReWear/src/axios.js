import axios from 'axios'

const API = import.meta.env.VITE_API_BASE_URL

const axiosInstance = axios.create({
  baseURL: API,
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: false,
})

export default axiosInstance
