import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import axios from 'axios'

export default function ItemPage() {
  const { id } = useParams()
  const [item, setItem] = useState(null)
  const [error, setError] = useState(null)
  const API = import.meta.env.VITE_API_BASE_URL

  useEffect(() => {
    const fetchItem = async () => {
      try {
        const res = await axios.get(`${API}/items/${id}`)
        setItem(res.data)
      } catch (err) {
        setError('Failed to load item.')
      }
    }
    fetchItem()
  }, [id])

  if (error) return <div className="text-center text-red-500 mt-8">{error}</div>
  if (!item) return <div className="text-center mt-8">Loading...</div>

  return (
    <div className="max-w-6xl mx-auto px-4 py-8">
      <div className="flex flex-col md:flex-row gap-8">
        <div className="flex-1">
          <img
            src={item.image_url}
            alt={item.title}
            className="w-full object-cover rounded-xl shadow"
          />
        </div>
        <div className="flex-1 space-y-4">
          <h1 className="text-3xl font-bold text-gray-800">{item.title}</h1>
          <p className="text-gray-600">{item.description}</p>
          <div className="grid grid-cols-2 gap-2 text-sm text-gray-700">
            <div><strong>Category:</strong> {item.category}</div>
            <div><strong>Size:</strong> {item.size}</div>
            <div><strong>Condition:</strong> {item.condition}</div>
            <div><strong>Status:</strong> {item.status}</div>
            <div className="col-span-2">
              <strong>Tags:</strong> {item.tags}
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
