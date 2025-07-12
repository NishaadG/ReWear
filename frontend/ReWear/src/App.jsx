// src/App.jsx
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Register from './pages/Register'
import Login from './pages/Login'
import Home from './pages/Home'
import ItemDetail from './pages/ItemDetail'
import UserDashboard from './pages/UserDashboard'
// … other imports

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/register" element={<Register />} />
         <Route path="/login"    element={<Login />} />
         <Route path="/home" element={<Home/>}/>
         <Route path="/item/:id" element={<ItemDetail />} />
         <Route path="/dashboard" element={<UserDashboard />} />
        {/* other routes */}
      </Routes>
    </BrowserRouter>
  )
}
