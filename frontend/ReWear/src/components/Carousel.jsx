export default function Carousel() {
  return (
    <section className="py-8 px-4 overflow-x-auto whitespace-nowrap">
      <h2 className="text-2xl font-semibold mb-4">Featured Items</h2>
      <div className="flex gap-4">
        {[...Array(5)].map((_, idx) => (
          <div key={idx} className="w-64 h-80 bg-gray-200 rounded-lg shadow-md inline-block"></div>
        ))}
      </div>
    </section>
  );
}
