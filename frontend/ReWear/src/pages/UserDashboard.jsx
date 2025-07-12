import { useEffect, useState } from 'react'
import axios from 'axios'

export default function UserDashboard() {
  const [user, setUser] = useState(null)
  const [error, setError] = useState('')

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const API = import.meta.env.VITE_API_BASE_URL
        const token = localStorage.getItem('token')
        const res = await axios.get(`${API}/me`, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        })
        setUser(res.data)
      } catch (err) {
        console.error(err)
        setError('Failed to load user data')
      }
    }

    fetchUser()
  }, [])

  if (error) {
    return <div className="text-red-500 p-4">{error}</div>
  }

  if (!user) {
    return <div className="text-center p-4">Loading...</div>
  }

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <div className="bg-white rounded-lg shadow-md p-6 max-w-4xl mx-auto">
        {/* Header Section */}
        <div className="flex items-center gap-6 mb-6">
          <div className="w-24 h-24 rounded-full bg-gray-300 flex-shrink-0" />
          <div className="grid grid-cols-2 gap-x-8 gap-y-2 flex-grow">
            <div><span className="font-semibold">Name:</span> {user.name}</div>
            <div><span className="font-semibold">Email:</span> {user.email}</div>
            <div><span className="font-semibold">Phone:</span> {user.phone}</div>
            <div><span className="font-semibold">Address:</span> {user.address}</div>
            <div><span className="font-semibold">Points:</span> {user.points}</div>
            <div><span className="font-semibold">Role:</span> {user.role}</div>
          </div>
        </div>

        {/* Placeholder for Description */}
        <div className="bg-gray-100 rounded-md p-4 text-gray-700 text-sm mb-8">
          Welcome to your dashboard. Here you can view your listings and purchases once implemented.
        </div>

        {/* Placeholder for My Listings */}
        <div className="mb-6">
          <h2 className="text-lg font-semibold mb-2">My Listings</h2>
          <div className="grid grid-cols-4 gap-4">
            {Array.from({ length: 4 }).map((_, idx) => (
              <div key={idx} className="bg-gray-200 h-32 rounded-lg"></div>
            ))}
          </div>
        </div>

        {/* Placeholder for My Purchases */}
        <div>
          <h2 className="text-lg font-semibold mb-2">My Purchases</h2>
          <div className="grid grid-cols-4 gap-4">
            {Array.from({ length: 4 }).map((_, idx) => (
              <div key={idx} className="bg-gray-200 h-32 rounded-lg"></div>
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}
