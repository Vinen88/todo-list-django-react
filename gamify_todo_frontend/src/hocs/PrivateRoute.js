import React from "react";
import { Route, Navigate, Outlet } from "react-router-dom";
import { connect } from "react-redux";
import PropTypes from "prop-types";

// const PrivateRoute = ({ component: Component, isAuthenticated, ...rest }) => (
//     <Route
//         {...rest}
//         render={props => isAuthenticated ? <Component {...props} /> : <Navigate to="/login" />}
//     />
// );

// const PrivateRoute = () => {
//     const { isAuthenticated } = this.props;
// }

// const mapStateToProps = state => ({
//      isAuthenticated: state.auth.isAuthenticated
// });

// export default connect(mapStateToProps, {})(PrivateRoute);