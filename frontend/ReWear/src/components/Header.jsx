export default function Header() {
  return (
    <header className="flex items-center justify-between p-4 bg-white shadow-md">
      <div className="text-xl font-bold">ReWear</div>
      <nav className="flex gap-6 text-sm font-medium">
        <a href="/home" className="hover:text-blue-600">Home</a>
        <a href="/browse" className="hover:text-blue-600">Browse</a>
        <a href="/login" className="hover:text-blue-600">Login</a>
        <a href="/register" className="hover:text-blue-600">Sign Up</a>
      </nav>
    </header>
  );
}
