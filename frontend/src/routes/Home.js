import CommonNavbar from "../components/navbar";

const Home = () => {
  return (
    <div onLoad={console.log(process.env.REACT_APP_TEST_ENV)}>
      <CommonNavbar />
      <h1>Welcome to Home</h1>
    </div>
  );
};

export default Home;
