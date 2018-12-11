import logging

logging.basicConfig(
    format='[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)

fixed = open('data/fixed.csv', 'a')
broken_lines = []

with open('data/oddetect.csv') as f:
    for index, line in enumerate(f):
        line_B = line.split(',')

        if len(line_B) == 14:
            fixed.write(line)
        else:
            logger.info(f"Broken line #{index}")
            broken_lines.append(index)

    logger.info(f"Broken lines #{len(broken_lines)}, Fixed lines {index - len(broken_lines)}")
