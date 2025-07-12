const BASE_URL = "http://localhost:8000";

export const fetchItems = async () => {
  const res = await fetch(`${BASE_URL}/items/`);
  return res.json();
};

export const fetchItemById = async (id) => {
  const res = await fetch(`${BASE_URL}/items/${id}`);
  return res.json();
};
