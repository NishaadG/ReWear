import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { fetchItemById } from "../api/api";
import Header from "../components/Header";

export default function ItemDetail() {
  const { id } = useParams();
  const [item, setItem] = useState(null);

  useEffect(() => {
    fetchItemById(id).then(setItem);
  }, [id]);

  if (!item) return <div className="p-6">Loading...</div>;

  return (
    <div>
      <Header />
      <div className="grid grid-cols-1 md:grid-cols-2 p-6 gap-8">
        <img src={item.images[0]} className="w-full h-96 object-cover rounded" />
        <div>
          <h2 className="text-2xl font-bold mb-2">{item.name}</h2>
          <p className="text-gray-700">{item.description}</p>
        </div>
      </div>

      <div className="p-6">
        <h3 className="text-lg font-semibold mb-2">More Images</h3>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          {item.images.map((img, idx) => (
            <img key={idx} src={img} className="h-40 w-full object-cover rounded" />
          ))}
        </div>
      </div>
    </div>
  );
}
