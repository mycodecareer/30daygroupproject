import React from "react";

import CommonNavbar from "../components/navbar";

const MyForm = () => {
  return (
    <>
      <CommonNavbar />
      <div class="container">
        <div class="row">
          <div class="col-3">
            <form>
              <div class="input-groupm my-auto mb-3">
                <label for="title">Recipe Title</label>
                <input
                  type="text"
                  name="title"
                  id="title"
                  placeholder="Enter recipe title"
                  class="form-control"
                />
              </div>
              <div class="input-groupm my-auto mb-3">
                <label for="author">Author</label>
                <input
                  class="form-control"
                  type="text"
                  name="author"
                  id="author"
                  placeholder="Author's name"
                />
              </div>
              <div class="input-groupm my-auto mb-3">
                <label for="description">Description</label>
                <textarea
                  class="form-control"
                  type="description"
                  name="description"
                  id="description"
                  placeholder="Recipe's description"
                  style={{ resize: "none" }}
                />
              </div>
              <button class="btn btn-primary">Submit</button>
            </form>
          </div>
        </div>
      </div>
    </>
  );
};

export default MyForm;
