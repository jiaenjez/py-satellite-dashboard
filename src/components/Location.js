import React from "react";
import ReactDOM from "react-dom";
import { useFormik } from "formik";
import "./styles.css";


const AddressForm = () => {
    const formik = useFormik({
    initialValues: { address: "", latLong: "" },
    onSubmit: values => {
        alert(JSON.stringify(formik.values.address, null, 2));
        fetch('/location',{
            method: 'POST',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                address: formik.values.address
            })
        })
            .then(res => res.json()).then(data => {
                formik.setFieldValue("latLong", JSON.stringify(data))
                console.log(JSON.stringify(formik.values.latLong))
            });
        alert(JSON.stringify(formik.values.latLong, null, 2));
    }
    });

return (
    <form onSubmit={formik.handleSubmit}>
        <label htmlFor="text">Address</label>
        <input
            id="address"
            name="address"
            type="text"
            onChange={formik.handleChange}
            value={formik.values.address}
        />
        <button type="submit">Submit</button>
        <p>{formik.values.address} is at {formik.values.latLong}.</p>
    </form>
    );
};

function Location() {
    return <AddressForm />;
}

const rootElement = document.getElementById("root");
ReactDOM.render(<Location />, rootElement);
export default Location;
