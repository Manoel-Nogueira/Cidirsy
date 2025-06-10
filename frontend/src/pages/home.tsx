import React from "react";
import { Background } from "../components/background";
import { Label } from "../components/label";
import { Navbar } from "../components/navbar"
import { Autocomplete, Box, Chip, Tab, Tabs, TextField } from "@mui/material";
import { Button } from "../components/button";

/*  Colors:
*   
*   #FFFFFF  
*   #33984b
*   #fbd916
* 
*/ 


export function Home () {

    const [value, setValue] = React.useState(0)
    const handleChange = (e: React.SyntheticEvent, newValue: number) => {setValue(newValue)}

    const symptoms = [

        {
            "id": 1,
            "symptom": "Folhas pretas"
        },
        {
            "id": 2,
            "symptom": "Queda dos frutos"
        },
        {
            "id": 3,
            "symptom": "Queda das folhas"
        },
        {
            "id": 4,
            "symptom": "Emrolamento das folhas"
        },
        {
            "id": 5,
            "symptom": "Caminhos em ziguezague na folha"
        },
        {
            "id": 6,
            "symptom": "Casca do tronco rachado"
        },
        {
            "id": 7,
            "symptom": "Tronco com manchas esbranquiçadas"
        },
        {
            "id": 8,
            "symptom": "Morte de galhos"
        },
        {
            "id": 9,
            "symptom": "Furos no tronco"
        },
        {
            "id": 10,
            "symptom": "Murchamento dos ramos"
        },

    ]

    console.log(value)

    return (

        <div className="h-screen w-full">

            <div>
                <Background className="opacity-75 blur-[0.094rem]"/>
            </div>

            <div className="relative z-10 flex">

                <nav className="shadow-md shadow-slate-600 fixed w-full">
                    <Navbar></Navbar>
                </nav>


                <main className="bg-[#FFFFFF] w-[100%] rounded-md mx-28 my-20 mt-[12rem] p-10">
                   
                    <div>
                        <Box sx={{ width: "100%", bgcolor: "background.paper"}}>
                            <Tabs value={value} onChange={handleChange} centered>
                                <Tab label="Cidirsy" sx={{fontWeight: "bold"}}/>
                                <Tab label="Item Two" sx={{fontWeight: "bold"}}/>
                                <Tab label="Item Three" sx={{fontWeight: "bold"}}/>
                            </Tabs>
                        </Box>                        
                    </div>

                    <div className="mt-15">

                        {value == 0 &&

                            <div className="flex flex-col justify-center items-center">

                                <div className="mb-5">
                                    <Label className="text-slate-600 text-3xl">Saiba Qual é a Doença do Seu Citrus Aqui</Label>
                                </div>

                                <div className="w-[50rem]">
                                    <Autocomplete multiple id="autocomplete" options={symptoms} getOptionLabel={(option) => option.symptom}
                                        renderInput={(params) => (<TextField {...params} variant="outlined" label="Sintomas" placeholder="Escolha um Sintoma"/>)}
                                    />
                                </div>

                                <div className="mt-5">
                                    <Button type="submit" className="bg-[#16824A] hover:bg-[#0F5832] active:bg-[#16824A] text-[#FFFFFF] items-center font-bold uppercase">Enviar</Button>
                                </div>

                                <div className="mt-5">
                                    <Label className="text-slate-600 text-2xl"> Doença:</Label>
                                </div>

                            </div>
                        }

                    </div>


                </main>


            </div>
            

        </div>

    )

}