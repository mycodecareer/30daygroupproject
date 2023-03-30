import { Link } from "react-router-dom";

const Home = () => {
  return (
    <div>
      <h1>Welcome to Home</h1>
      <Link to="/form">Go to Form</Link>
    </div>
  );
};

export default Home;
