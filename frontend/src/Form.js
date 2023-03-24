import React from "react";
import {
  Button,
  Form,
  FormGroup,
  Input,
  Label,
  Container,
  Row,
  Col,
} from "reactstrap";
import "bootstrap/dist/css/bootstrap.min.css";

const MyForm = () => {
  return (
    <Container>
      <Form>
        <FormGroup>
          <Label for="title">Recipe Title</Label>
          <Input
            type="text"
            name="title"
            id="title"
            placeholder="Enter recipe title"
          />
        </FormGroup>
        <FormGroup>
          <Label for="author">Author</Label>
          <Input
            type="text"
            name="author"
            id="author"
            placeholder="Author's name"
          />
        </FormGroup>
        <FormGroup>
          <Label for="description">Description</Label>
          <Input
            type="description"
            name="description"
            id="description"
            placeholder="Recipe's description"
          />
        </FormGroup>
        <Button color="primary">Submit</Button>
      </Form>
    </Container>
  );
};

export default MyForm;
