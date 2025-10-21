package com.example.apartamentos.controllers;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import com.example.apartamentos.models.PropiedadImagen;
import com.example.apartamentos.services.PropiedadImagenService;

@RestController
@RequestMapping("/api/imagenes")
@CrossOrigin(origins = "*")
public class PropiedadImagenController {

    @Autowired
    private PropiedadImagenService imagenService;

    @GetMapping
    public List<PropiedadImagen> getAllImagenes() {
        return imagenService.getAllImagenes();
    }

    @GetMapping("/{id}")
    public Optional<PropiedadImagen> getImagenById(@PathVariable Long id) {
        return imagenService.getImagenById(id);
    }

    @PostMapping
    public PropiedadImagen saveImagen(@RequestBody PropiedadImagen imagen) {
        return imagenService.saveImagen(imagen);
    }

    @DeleteMapping("/{id}")
    public void deleteImagen(@PathVariable Long id) {
        imagenService.deleteImagen(id);
    }
}

