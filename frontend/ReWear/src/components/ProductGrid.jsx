export default function ProductGrid() {
  return (
    <section className="px-4 py-8">
      <h2 className="text-xl font-semibold mb-4">Product Listings</h2>
      <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4">
        {[...Array(8)].map((_, idx) => (
          <div key={idx} className="bg-white border rounded-lg shadow p-4 h-64">
            <div className="bg-gray-200 h-40 mb-2 rounded"></div>
            <h3 className="font-medium">Product {idx + 1}</h3>
            <p className="text-sm text-gray-500">Description</p>
          </div>
        ))}
      </div>
    </section>
  );
}
