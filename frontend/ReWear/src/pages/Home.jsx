import { useEffect, useState } from 'react';
import axios from 'axios';

export default function Home() {
  const [items, setItems] = useState([]);
  const [categories, setCategories] = useState([]);
  const [images, setImages] = useState([]);

  useEffect(() => {
    const fetchItems = async () => {
      try {
        const API = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';
        const res = await axios.get(`${API}/get/items`);
        const data = res.data;

        setItems(data.slice(0, 4)); // Just a few for "Product Listings"
        setImages(shuffleArray(data).slice(0, 1)); // One large image
        const uniqueCategories = [...new Set(data.map((item) => item.category))];
        setCategories(uniqueCategories.slice(0, 6)); // Limit to first 6 categories
      } catch (err) {
        console.error('Failed to fetch items:', err);
      }
    };

    fetchItems();
  }, []);

  const shuffleArray = (array) => {
    return [...array].sort(() => Math.random() - 0.5);
  };

  return (
    <div className="min-h-screen bg-gray-50 py-8 px-6">
      <div className="max-w-6xl mx-auto space-y-10">
        {/* Images Section */}
        <div>
          <h2 className="text-2xl font-semibold text-gray-800 mb-3">Images</h2>
          <div className="w-full h-64 bg-gray-200 rounded-lg overflow-hidden">
            {images[0] && (
              <img
                src={images[0].image_url}
                alt="featured"
                className="w-full h-full object-cover"
              />
            )}
          </div>
        </div>

        {/* Categories Section */}
        <div>
          <h2 className="text-2xl font-semibold text-gray-800 mb-3">Categories</h2>
          <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-6 gap-4">
            {categories.map((cat, i) => (
              <div
                key={i}
                className="bg-white shadow p-3 rounded-lg text-center font-medium text-teal-600 capitalize"
              >
                {cat}
              </div>
            ))}
          </div>
        </div>

        {/* Product Listings */}
        <div>
          <h2 className="text-2xl font-semibold text-gray-800 mb-3">Product Listings</h2>
          <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-5">
            {items.map((item) => (
              <div
                key={item.id}
                className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-xl transition"
              >
                <img
                  src={item.image_url}
                  alt={item.title}
                  className="w-full h-40 object-cover"
                />
                <div className="p-4">
                  <h3 className="text-lg font-semibold text-gray-800 truncate">
                    {item.title}
                  </h3>
                  <p className="text-sm text-gray-500">{item.category}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
