export default function Hero() {
  return (
    <section className="text-center py-10 bg-gray-100">
      <h1 className="text-4xl font-bold mb-4">Swap Clothes. Save the Planet.</h1>
      <p className="mb-6 text-gray-600">Join the circular fashion movement today.</p>
      <div className="flex justify-center gap-4">
        <button className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700">Start Swapping</button>
        <button className="border border-blue-600 text-blue-600 px-6 py-2 rounded hover:bg-blue-100">Browse Items</button>
      </div>
    </section>
  );
}
