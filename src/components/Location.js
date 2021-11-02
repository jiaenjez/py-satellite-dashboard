import React from "react";
import ReactDOM from "react-dom";
import { useFormik } from "formik";
import "./styles.css";


const AddressForm = () => {
    const formik = useFormik({
    initialValues: { address: "", latLong: "" , city: "", postalCode: "", country: "", adminDistrict:""},
    onSubmit: values => {
        alert(JSON.stringify(formik.values.address, null, 2));
        fetch('/location',{
            method: 'POST',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                address: formik.values.address,
                city: formik.values.city,
                postalCode: formik.values.postalCode,
                country: formik.values.country,
                adminDistrict: formik.values.adminDistrict
            })
        })
            .then(res => res.json()).then(data => {
                formik.setFieldValue("latLong", JSON.stringify(data))
                console.log(formik.values.latLong)
            });
        alert(JSON.stringify(formik.values.latLong, null, 2));
    }
    });

return (
    <form onSubmit={formik.handleSubmit}>
        <label htmlFor="text">Street Address</label>
        <input
            id="address"
            name="address"
            type="text"
            onChange={formik.handleChange}
            value={formik.values.address}
        />

        <label htmlFor="text">City</label>
        <input
            id="city"
            name="city"
            type="text"
            onChange={formik.handleChange}
            value={formik.values.city}
        />

        <label htmlFor="text">postalCode</label>
        <input
            id="postalCode"
            name="postalCode"
            type="text"
            onChange={formik.handleChange}
            value={formik.values.postalCode}
        />

        <label htmlFor="text">Country</label>
        <input
            id="country"
            name="country"
            type="text"
            onChange={formik.handleChange}
            value={formik.values.country}
        />

        <label htmlFor="text">adminDistrict</label>
        <input
            id="adminDistrict"
            name="adminDistrict"
            type="text"
            onChange={formik.handleChange}
            value={formik.values.adminDistrict}
        />


        <button type="submit">Submit</button>
        <p>{formik.values.address}, {formik.values.city}, {formik.values.adminDistrict}, {formik.values.postalCode}, {formik.values.country} is at {formik.values.latLong}.</p>
    </form>
    );
};

function Location() {
    return <AddressForm />;
}

const rootElement = document.getElementById("root");
ReactDOM.render(<Location />, rootElement);
export default Location;
