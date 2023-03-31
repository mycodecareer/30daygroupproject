import React, { useEffect, useState, useCallback } from "react";

const API_ENDPOINT = "https://www.themealdb.com/api/json/v1/1/random.php";

const Random = () => {
  const [data, setData] = useState({});

  const fetchRecipe = useCallback(async () => {
    try {
      const response = await fetch(API_ENDPOINT);
      const recipe = await response.json();
      setData(recipe);
    } catch (err) {
      console.error(err);
    }
  }, []);

  useEffect(() => {
    fetchRecipe();
  }, [fetchRecipe]);

  return (
    <div>
      {data.meals ? (
        <p>{JSON.stringify(data.meals)}</p>
      ) : (
        <p>Loading recipe...</p>
      )}
    </div>
  );
};

export default Random;
