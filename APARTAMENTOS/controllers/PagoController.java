package com.example.apartamentos.controllers;

import com.example.apartamentos.models.Pago;
import com.example.apartamentos.services.PagoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/pagos")
public class PagoController {

    @Autowired
    private PagoService pagoService;

    // ✅ Obtener todos los pagos
    @GetMapping
    public List<Pago> getAllPagos() {
        return pagoService.getAllPagos();
    }

    // ✅ Obtener un pago por ID
    @GetMapping("/{id}")
    public ResponseEntity<Pago> getPagoById(@PathVariable Integer id) {
        Optional<Pago> pago = pagoService.getPagoById(id);
        return pago.map(ResponseEntity::ok)
                   .orElseGet(() -> ResponseEntity.notFound().build());
    }

    // ✅ Crear un nuevo pago
    @PostMapping
    public Pago createPago(@RequestBody Pago pago) {
        return pagoService.savePago(pago);
    }

    // ✅ Actualizar un pago existente
    @PutMapping("/{id}")
    public ResponseEntity<Pago> updatePago(@PathVariable Integer id, @RequestBody Pago pagoDetails) {
        Optional<Pago> pagoOptional = pagoService.getPagoById(id);
        if (pagoOptional.isPresent()) {
            Pago pagoToUpdate = pagoOptional.get();
            pagoToUpdate.setMonto(pagoDetails.getMonto());
            pagoToUpdate.setMetodoPago(pagoDetails.getMetodoPago());
            pagoToUpdate.setEstado(pagoDetails.getEstado());
            pagoToUpdate.setFechaPago(pagoDetails.getFechaPago());
            pagoToUpdate.setReferenciaPago(pagoDetails.getReferenciaPago());
            pagoToUpdate.setDatosPago(pagoDetails.getDatosPago());
            pagoToUpdate.setReservacion(pagoDetails.getReservacion());

            Pago updatedPago = pagoService.savePago(pagoToUpdate);
            return ResponseEntity.ok(updatedPago);
        } else {
            return ResponseEntity.notFound().build();
        }
    }

    // ✅ Eliminar un pago
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deletePago(@PathVariable Integer id) {
        Optional<Pago> pago = pagoService.getPagoById(id);
        if (pago.isPresent()) {
            pagoService.deletePago(id);
            return ResponseEntity.noContent().build();
        } else {
            return ResponseEntity.notFound().build();
        }
    }
}
