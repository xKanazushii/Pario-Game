   def run(self):
        while True:
            dt = self.clock.tick(144) /  1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.current_stage.run(dt)