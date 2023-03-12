import "./App.css";

function handleHeaderClick() {
  const header = document.getElementById("myHeader");
  header.style.top = "-200px";
  setTimeout(function () {
    header.style.display = "none";
  }, 5000);
}

function Header() {
  return (
    <div className="header">
      <header id="myHeader" onClick={handleHeaderClick}>
        <h1 class="logo">SageChat</h1>
        <h2 class="tagline">"Where compassion meets conversation"</h2>
        <figure class="header-image">
          <img
            src="https://cdn.dribbble.com/users/1358255/screenshots/4951199/media/90d725c5822d477ec1fa763357e00988.png?compress=1&resize=800x600&vertical=top"
            alt="old man logo"
          ></img>
        </figure>
        <script></script>
      </header>
    </div>
  );
}

export default Header;