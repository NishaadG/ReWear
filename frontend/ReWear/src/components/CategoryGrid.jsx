export default function CategoryGrid() {
  return (
    <section className="px-4 py-8">
      <h2 className="text-xl font-semibold mb-4">Categories</h2>
      <div className="grid grid-cols-3 sm:grid-cols-4 gap-4">
        {["Tops", "Bottoms", "Dresses", "Accessories", "Shoes", "Winter"].map((category, idx) => (
          <div key={idx} className="bg-blue-100 text-center py-6 rounded shadow-sm hover:bg-blue-200 cursor-pointer">
            {category}
          </div>
        ))}
      </div>
    </section>
  );
}
