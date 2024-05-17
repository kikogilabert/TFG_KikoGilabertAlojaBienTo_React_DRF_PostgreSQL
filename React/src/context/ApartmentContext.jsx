import React, {useState, useEffect} from "react";
import ApartmentService from "../services/ApartmentService";

const Context = React.createContext({});

export function ApartmentContextProvider({children}) {
    const [apartments, setApartments] = useState([]);
    const [ shouldUpdate, setShouldUpdate ] = useState(false);

    useEffect(() => {
        ApartmentService.getAllApartments()
            .then(response => {
                setApartments(response.data);
                console.log(response.data);
            })
            .catch(e => {
                console.log(e);
            });
    }, [setApartments]);

    return (
        <Context.Provider value={{apartments, setApartments}}>
            {children}
        </Context.Provider>
    );
}
export default Context;